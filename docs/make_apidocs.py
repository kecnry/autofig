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

def api_docs(item, skip=[], prefix='', subclass_of=None, write=True, members=[pydoc.inspect.isclass, pydoc.inspect.ismethod, pydoc.inspect.isfunction, pydoc.inspect.isdatadescriptor]):
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

    fms = api_docs(autofig.figure, prefix='autofig')
    fms = api_docs(autofig.figure.Figure, prefix='autofig.figure')

    fms = api_docs(autofig.axes, prefix='autofig', skip=['Axes3D', 'LineCollection'])
    fms = api_docs(autofig.axes.AxesGroup, prefix='autofig.axes')
    fms = api_docs(autofig.axes.Axes, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionGroup, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionCGroup, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionSGroup, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxArray, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimension, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionI, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionX, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionY, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionZ, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionScale, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionS, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxDimensionC, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxViewGroup, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxView, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxViewElev, prefix='autofig.axes')
    fms = api_docs(autofig.axes.AxViewAzim, prefix='autofig.axes')


    fms = api_docs(autofig.call, prefix='autofig', skip=['Axes3D', 'LineCollection', 'Line3DCollection', 'PolyCollection', 'Poly3DCollection', 'make_callgroup', 'make_calldimensiongroup'])
    fms = api_docs(autofig.call.CallGroup, prefix='autofig.call', skip=['connect_callback'])
    fms = api_docs(autofig.call.PlotGroup, prefix='autofig.call', skip=['connect_callback'])
    fms = api_docs(autofig.call.MeshGroup, prefix='autofig.call', skip=['connect_callback'])
    fms = api_docs(autofig.call.Call, prefix='autofig.call', skip=['connect_callback'])
    fms = api_docs(autofig.call.Plot, prefix='autofig.call', skip=['connect_callback'])
    fms = api_docs(autofig.call.Mesh, prefix='autofig.call', skip=['connect_callback'])
    fms = api_docs(autofig.call.CallDimensionGroup, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionCGroup, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionSGroup, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimension, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionI, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionX, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionY, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionZ, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionS, prefix='autofig.call')
    fms = api_docs(autofig.call.CallDimensionC, prefix='autofig.call')
