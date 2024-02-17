from option import src as s
from lib import FormatMaker as FM
from sys import argv as a


def main():
  x = a[2] if len(a) > 2 else 'webtoon'
  fn = a[1].split('.')
  fn.pop()
  fn = '.'.join(fn)
  fn += '.html'
  with open(fn, 'w') as fp:
    fp.write(a[1].splitFM(s)(a[1], x))


if __name__ == '__main__': main()
