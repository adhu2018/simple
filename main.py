from pathlib import Path
import shutil

def get_name(name):
    _n = name.split('-')
    if len(_n)==1:
        return ''
    return _n[0]

def move_file(path):
    p = Path(path)
    n_p = Path().joinpath(p.name)
    shutil.move(p, n_p)
    p = n_p
    if p.is_file():
        _n = get_name(p.name)
        if _n:
            _d = _n.replace('_', '-').lower()
            _d = _n.replace('.', '-')
            _d = Path().joinpath(_d)
            if _d.exists():
                if _d.is_file():
                    print(_d,"is file.")
                    return
            else:
                _d.mkdir()
    n_p = Path(_d).joinpath(p.name)
    shutil.move(p, n_p)

def _make_index(dir, name):
    r = "<!DOCTYPE html>\n"\
        + "<html>\n"\
        + "<head>\n"\
        + f"    <title>{dir.name} Index</title>\n"\
        + "</head>\n"\
        + "<body>\n"
    for n in name:
        r += f"    <a href='{n.name}'>{n.name}</a><br>\n"
    r += "</body>\n"\
        + "</html>"
    rf = dir.joinpath("index.html")
    with open(rf, "w", encoding="utf8") as f:
        f.write(r)
    return rf

def make_index():
    dl = list(Path().glob('**/'))
    dl1 = []
    for d in dl:
        fl1 = list(d.glob('*.whl'))
        fl2 = list(d.glob('*.gz'))
        fl1.extend(fl2)
        if fl1:
            _make_index(d, fl1)
            dl1.append(d)
    _make_index(Path().cwd(), dl1)

def main():
    w = list(Path().glob('**/*.whl'))
    g = list(Path().glob('**/*.gz'))
    w.extend(g)
    for i in w:
        move_file(i)
    make_index()

if __name__=="__main__":
    main()
