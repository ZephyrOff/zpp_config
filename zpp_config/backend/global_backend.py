class ConfigBackend:
    """Classe abstraite pour les backends de configuration."""
    def load(self, filename):
        raise NotImplementedError()

    def load_data(self, rendered):
        """Parse une chaîne rendue (Jinja) et retourne un dict."""
        raise NotImplementedError()

    def save(self, filename, data):
        raise NotImplementedError()
