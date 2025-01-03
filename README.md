# mkdocs-material-extras

A plugin for MKDocs - specifically the [MKDocs Material Theme](https://squidfunk.github.io/mkdocs-material/).

This small plugin adds additional resources such as styles, scripts, and helpers for Project Documentation, helping with some of my projects. Heavily inspired by [@facelessuser](https://github.com/facelessuser)'s [mkdocs_pymdownx_material_extras](https://github.com/facelessuser/mkdocs_pymdownx_material_extras).

> [!NOTE]  
> While this was originally developed for my own projects, it can still be freely used if desired.

## Installation

The project is availbale on [PyPI](https://pypi.org) as a Pythpn Package. Set up a [Virtual Enviroment](https://docs.python.org/3/library/venv.html) (Highly Recommended), and then install it with

``` sh
pip install mkdocs-material-extras
```

Next, add it to your list of MKDocs plugins. When doing so, remember to include search in the list of plugins as it doesn't append to the plugins, but overrides the plugins:

``` yaml
plugins:
  - search
  - mkdocs_material_extras
```

## Usage

## Features

### Announcement Bar

Create a new file at the root of your overrides folder, and name it `announcements.html`. You can now place in your desired content, just be sure it's legitimate HTML.

``` html
For updates follow <strong>@squidfunk</strong> on
<a rel="me" href="https://fosstodon.org/@squidfunk">
  <span class="twemoji mastodon">
    {% include ".icons/fontawesome/brands/mastodon.svg" %}
  </span>
  <strong>Fosstodon</strong>
</a>
and
<a href="https://x.com/squidfunk">
  <span class="twemoji twitter">
    {% include ".icons/fontawesome/brands/twitter.svg" %}
  </span>
  <strong>Twitter</strong>
</a>
```

### Including Libraries

Create a new folder named `partials`. Within that folder, create a file called `libs.html`. You can now place and link your JavaScript libraries.

``` html
<script src="{{ 'main.js' | url }}" type="text/javascript"></script>
<script src="{{ 'custom.js' | url }}" type="text/javascript"></script>
```

## About This Project