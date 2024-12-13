import inkex
import datetime

class ResetToStdConfig(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.log_file = 'extension_log.txt'
        self.enable_logging = False

    def effect(self):
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(f"--- ResetToStdConfig ---\n")
                f.write(f"{datetime.datetime.now()}\n")

        # Select layers using XPath
        all_layers = self.svg.xpath('//svg:g[@inkscape:groupmode="layer"]')

        # 1. Hide all layers initially
        for layer in all_layers:
            self.set_layer_visibility(layer, False)
            self.print_to_log(f"Hid layer: {layer.get(inkex.addNS('label', 'inkscape'))}")

        # 2. Identify and show standard layers and their parents
        for layer in all_layers:
            if "(STD)" in layer.get(inkex.addNS('label', 'inkscape'), ''):
                self.set_layer_visibility(layer, True)
                self.print_to_log(f"Showed layer: {layer.get(inkex.addNS('label', 'inkscape'))}")
                self.show_parent_layers(layer)

        # 3. Lock all layers and unlock "SCRATCH LAYER (STD)"
        self.lock_and_unlock_layers()

        # 4. Update the SVG document
        self.document.write(self.options.input_file)

        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write('\n\n')

    def get_all_layers(self, svg):
        """Recursively finds all layers in the SVG document."""
        layers = []
        for element in svg:
            if element.get(inkex.addNS('groupmode', 'inkscape')) == 'layer':
                layers.append(element)
                layers.extend(self.get_all_layers(element))
        return layers

    def set_layer_visibility(self, layer, visible):
        """Sets the visibility of a layer."""
        if visible:
            layer.set('style', 'display:inline;')
        else:
            layer.set('style', 'display:none;')

    def show_parent_layers(self, layer):
        """Recursively makes all parent layers of a layer visible."""
        parent = layer.getparent()
        if parent is not None and parent.get(inkex.addNS('groupmode', 'inkscape')) == 'layer':
            self.set_layer_visibility(parent, True)
            self.print_to_log(f"Showed parent layer: {parent.get(inkex.addNS('label', 'inkscape'))}")
            self.show_parent_layers(parent)

    def lock_and_unlock_layers(self):
        """Locks all layers and unlocks the "SCRATCH LAYER (STD)" layer."""
        try:
            # Select all layers using XPath
            layers = self.svg.xpath('//svg:g[@inkscape:groupmode="layer"]')

            # Lock all layers
            for layer in layers:
                layer.set('sodipodi:insensitive', 'true')

            # Unlock "SCRATCH LAYER (STD)"
            scratch_layer = self.svg.xpath(f'//svg:g[@inkscape:label="SCRATCH LAYER (STD)"]')
            if scratch_layer:
                scratch_layer[0].set('sodipodi:insensitive', None)

        except Exception as e:
            self.print_to_log(f"Error locking/unlocking layers: {e}")

    def print_to_log(self, message):
        """Prints a message to the log file if logging is enabled."""
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(message + '\n')
                
if __name__ == '__main__':
    ResetToStdConfig().run()
