# Plugin Src
# This plugin imports extra css and javascript to the theme, as well as allowing templates to be defined in the plugin itself.

import glob
import os
import mkdocs.plugins

RESOURCE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'theme')

class MkdocsMaterialExtends(mkdocs.plugins.BasePlugin):
    def on_config(self, config, **kwargs):
        config['theme'].dirs.insert(0, RESOURCE_PATH)
        base_path = RESOURCE_PATH.replace('\\', '/') + '/'

        # Helper Function: Adds extra CSS to the theme.
        extras = set(config['extra_css'])
        for f in glob.glob(base_path + '**/*.css', recursive=True):
            name = f.replace('\\', '/').replace(base_path, '')
            if name not in extras:
                config['extra_css'].append(name)

        # Another Helper Function: Adds extra JavaScripts to theme theme.
        extras = set(config['extra_javascript'])
        for f in glob.glob(base_path + '**/*.js', recursive=True):
            name = f.replace('\\', '/').replace(base_path, '')
            if name not in extras:
                config['extra_javascript'].append(name)

        return config