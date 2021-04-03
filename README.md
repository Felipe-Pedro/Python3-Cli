# Introduction

Python3-Cli is a library focused in make cli programs with python3 (obviously). The ideia is, you have an cli object which you can interact, and it will take care of everything, even the app loop.

# Features

- [x] Regular scene
- [x] Table scene
- [ ] Help scene
- [ ] Auth scene

# Dependencies

* Pandas

Pandas is required to make and who the tables

# How it works

1. Import and create the cli object.
  ```python
  from Cli import cli
  
  cli = cli()
  ```
2. Add as many scenes as you want.
  ```python
  cli.add_scene("wellcome_scene", ["See information", "Go to table"], "Wellcome to the app, fell free to explore", ["info_scene", "table_scene"])
  cli.add_scene("info_scene", ["Back to the wellcome scene"], "This is an example app :)", ["wellcome_scene"])
  cli.add_table_scene("table_scene", ["Back to the wellcome scene"], {"Column1": ["Line1", "Line2", "Line3"]}, ["wellcome_scene"])
  ```
3. Set the first scene which will be shown.
  ```python
  cli.set_first_scene_name("wellcome_scene")
  ```
4. Start the app loop.
  ```python
  cli.render_forever()
