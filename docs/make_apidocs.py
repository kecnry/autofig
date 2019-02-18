import pydoc
import os, sys, shutil
import re

def md_internal_link(matchobj):
    text = matchobj.group(0)
    path = text[4:-4]
    return "[{}]({}.md)".format(path, path)

def get_kind(item):
    kind = ''
    if pydoc.inspect.isclass(item):
        kind = 'class'
    elif pydoc.inspect.ismodule(item):
        kind = 'module'
    elif pydoc.inspect.ismethod(item):
        kind = 'method'
    elif pydoc.inspect.isfunction(item):
        kind = 'function'
    elif pydoc.inspect.isdatadescriptor(item):
        kind = 'property'

    return kind

def api_docs(item, skip=[], prefix='', subclass_of=None, write=True, members=[pydoc.inspect.ismethod, pydoc.inspect.isfunction, pydoc.inspect.isdatadescriptor]):
    def check_member(item):
        for member in members:
            if member(item):
                return True

        return False

    # item is either a module or class
    stored_fms = []

    for fm in pydoc.inspect.getmembers(item, check_member):
        output = list()

        if fm[0] in skip or (fm[0].startswith('_') and fm[0] != '__init__'):
            continue

        if pydoc.inspect.ismodule(fm[1]) or pydoc.inspect.isclass(fm[1]):
            stored_fms.append(fm[0])
            # don't write its own page, make a manual call to api_docs to do that... but we will create the link
            continue

        path = [p for p in prefix.split(".")+[item.__name__.split(".")[-1]] if len(p)]
        path_md = ".".join(["[{}]({}.md)".format(p, ".".join(path[:i+1])) for i,p in enumerate(path)])
        output.append("### {}.{} ({})\n\n".format(path_md, fm[0], get_kind(fm[1])))

        # Get the signature
        if pydoc.inspect.ismethod(fm[1]) or pydoc.inspect.isfunction(fm[1]):
            output.append ('```py\n')
            output.append('def %s%s\n' % (fm[0], pydoc.inspect.formatargspec(*pydoc.inspect.getargspec(fm[1]))))
            output.append ('```\n')

        # get the docstring
        if pydoc.inspect.getdoc(fm[1]):
            output.append('\n')
            docstring = pydoc.HTMLDoc().markup(pydoc.inspect.getdoc(fm[1]))
            docstring = re.sub(r"(?P<name>&lt;[0a-zA-Z_\.]*&gt;)", md_internal_link, docstring)
            output.append(docstring)

        output.append('\n')


        stored_fms.append(fm[0])

        if write:
            path = ".".join([p for p in prefix.split(".") if len(p)]+[item.__name__.split(".")[-1], fm[0]])

            filename = './api/{}.md'.format(path)
            print("writing {}".format(filename))
            f_method = open(filename, 'w')
            f_method.write("\n".join(output))
            f_method.close()

    if write:
        path = [p for p in prefix.split(".")+[item.__name__.split(".")[-1]] if len(p)]
        path_md = ".".join(["[{}]({}.md)".format(p, ".".join(path[:i+1])) for i,p in enumerate(path[:-1])])
        if len(path_md):
            path_md += ".{}".format(item.__name__.split(".")[-1])
        else:
            path_md = item.__name__.split(".")[-1]

        path = ".".join(path)
        filename_class = './api/{}.md'.format(path)
        print("writing {}".format(filename_class))
        f_class = open(filename_class, 'w')
        f_class.write("## {} ({})\n\n".format(path_md, get_kind(item)))
        if subclass_of is not None:
            f_class.write("{} is a subclass of {} and therefore also includes all [{} methods]({}.md)\n\n".format(item.__name__, subclass_of, subclass_of, subclass_of))
        if hasattr(item, '__doc__') and item.__doc__ is not None:
            for l in item.__doc__.split("\n"):
                docstringline = pydoc.HTMLDoc().markup(l.lstrip()+"\n")
                docstringline = re.sub(r"(?P<name>&lt;[0a-zA-Z_\.]*&gt;)", md_internal_link, docstringline)
                f_class.write(docstringline)
            f_class.write("\n\n")
        for fm in stored_fms:
            path_fm = ".".join([p for p in prefix.split(".") if len(p)]+[item.__name__.split(".")[-1], fm])
            f_class.write("* [{}]({}.md)\n".format(fm, path_fm))
        f_class.close()

    return stored_fms


if __name__ == '__main__':
    import autofig

    print("CREATING API DOCS FOR AUTOFIG VERSION: {}".format(autofig.__version__))

    fms = api_docs(autofig, skip=[], members=[pydoc.inspect.isfunction])
    shutil.copyfile('./api/autofig.md', './api/index.md')

    skip_methods = []
    fms = api_docs(autofig.Axes, skip=skip_methods)
    fms = api_docs(autofig.Figure, skip=skip_methods)
    fms = api_docs(autofig.Plot, skip=skip_methods)
    fms = api_docs(autofig.Mesh, skip=skip_methods)
