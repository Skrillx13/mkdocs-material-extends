import os
import glob
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from csscompressor import compress as compress_css
from jsmin import jsmin as compress_js

class MaterialExtendsPlugin(BasePlugin):
    config_scheme = (
        ('css_dir', config_options.Type(str, default='stylesheets')),
        ('js_dir', config_options.Type(str, default='javascripts')),
    )

    def on_config(self, config):
        # Path to the plugin directory
        plugin_dir = os.path.dirname(__file__)

        # Minify and add CSS files from stylesheets directory
        css_dir = os.path.join(plugin_dir, self.config['css_dir'])
        if os.path.exists(css_dir):
            for css_file in glob.glob(os.path.join(css_dir, '*.css')):
                with open(css_file, 'r', encoding='utf-8') as f:
                    minified_css = compress_css(f.read())
                minified_css_file = css_file.replace('.css', '.min.css')
                with open(minified_css_file, 'w', encoding='utf-8') as f:
                    f.write(minified_css)
                config['extra_css'].insert(0, os.path.relpath(minified_css_file, plugin_dir))

        # Minify and add JavaScript files from javascripts directory
        js_dir = os.path.join(plugin_dir, self.config['js_dir'])
        if os.path.exists(js_dir):
            for js_file in glob.glob(os.path.join(js_dir, '*.js')):
                with open(js_file, 'r', encoding='utf-8') as f:
                    minified_js = compress_js(f.read())
                minified_js_file = js_file.replace('.js', '.min.js')
                with open(minified_js_file, 'w', encoding='utf-8') as f:
                    f.write(minified_js)
                config['extra_javascript'].insert(0, os.path.relpath(minified_js_file, plugin_dir))

        return config