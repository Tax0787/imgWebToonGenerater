class FormatMaker:

  def __init__(self, html_form):
    self.__src = lambda x: html_form.format(
        '<link href="style.css" rel="stylesheet" />', x)

  def __call__(self, img, alt):
    return self.__src(f'<img src="{img}" alt="{alt}"/>')
