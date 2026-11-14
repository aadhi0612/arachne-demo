from mako.template import Template


def render_greeting(name):
    return Template("Hello ${name | h}!").render(name=name)
