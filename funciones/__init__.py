"""
Auto-importa símbolos públicos de cada módulo dentro de `funciones/`.
"""
import importlib, pkgutil
__all__ = []
for _f, _name, _is_pkg in pkgutil.iter_modules(__path__):
    if _is_pkg:
        continue
    m = importlib.import_module(f"{__name__}.{_name}")
    public = getattr(m, "__all__", None) or [n for n in dir(m) if not n.startswith("_")]
    for s in public:
        globals()[s] = getattr(m, s)
        __all__.append(s)
