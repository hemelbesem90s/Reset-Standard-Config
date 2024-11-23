# Inkscape Reset to Standard Configuration Extension

This extension resets the visibility of all layers in an Inkscape document to a predefined standard configuration.

## Functionality

The extension works with SVG files that have a hierarchical layer structure, where:

* Top-level layers represent option groups.
* Sub-layers represent specific options within those groups.
* Layers are made visible or invisible to enable or disable corresponding options.
* Layers that are part of the standard configuration have "(STD)" appended to their names.

The extension resets the visibility of all layers so that only the layers with "(STD)" in their names (and their parent layers) are visible.

## Usage

1. Install the extension by placing the `reset_to_std_config.inx` and `reset_to_std_config.py` files in your Inkscape extensions directory.
2. Open your SVG document in Inkscape.
3. Go to `Extensions > Layer > Reset to Standard Configuration`.

## Acknowledgements

This extension was developed with the help of [Gemini Advanced](https://sites.research.google/gemini), Google's next-generation AI model. 

Special thanks to the Inkscape community for their valuable contributions and support, particularly the following resources:

* Inkscape Forum: [https://inkscape.org/forums/](https://inkscape.org/forums/)
* Inkscape Wiki: [https://wiki.inkscape.org/wiki/](https://wiki.inkscape.org/wiki/)
* Inkscape Extensions Documentation: [https://inkscape.gitlab.io/extensions/documentation/](https://inkscape.gitlab.io/extensions/documentation/)

## License

This extension is licensed under the GNU General Public License v2.0. See the LICENSE file for details.
