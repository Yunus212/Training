>>> import sys # получим список атрибутов модуля 'sys'

>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__', '__s
tderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_compact_freelists',
'_current_frames', '_getframe', 'api_version', 'argv', 'builtin_module_names', '
byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle'
, 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable',
'exit', 'flags', 'float_info', 'getcheckinterval', 'getdefaultencoding', 'getfil
esystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof',
'gettrace', 'getwindowsversion', 'hexversion', 'intern', 'maxsize', 'maxunicode
', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platfor
m', 'prefix', 'ps1', 'ps2', 'setcheckinterval', 'setprofile', 'setrecursionlimit
', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_in
fo', 'warnoptions', 'winver']

>>> dir() # получим список атрибутов текущего модуля
['__builtins__', '__doc__', '__name__', '__package__', 'sys']

>>> a = 5 # создадим новую переменную 'a'

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a', 'sys']

>>> del a # удалим имя 'a'

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']

>>>