from .base_executor import ShellExecutor


class Executor(ShellExecutor):
    ext = '.sh'
    name = 'BASH'
    command = 'bash'
    command_paths = ['bash']
    test_program = 'exec cat'

    def get_cmdline(self):
        return ['bash', self._code]
