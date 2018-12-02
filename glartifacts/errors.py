class GitlabArtifactsError(Exception):
    pass

class NoProjectError(GitlabArtifactsError):
    pass

class InvalidConfigSectionError(GitlabArtifactsError):
    def __init__(self, config_file, section_name):
        super().__init__(
            '{}: Invalid config section {}'.format(
                config_file,
                section_name
                )
            )

class InvalidConfigOptionError(GitlabArtifactsError):
    def __init__(self, config_file, section_name, item_name):
        super().__init__(
            '{}: Invalid config option {}.{}'.format(
                config_file,
                section_name,
                item_name
                )
            )
