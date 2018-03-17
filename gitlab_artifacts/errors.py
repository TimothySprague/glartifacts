class GitlabArtifactsError(Exception):
    pass

class NoProjectError(GitlabArtifactsError):
    pass
