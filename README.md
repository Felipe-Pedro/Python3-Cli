# Introduction

Python3-Cli is a library focused in make cli programs with python3 (obviously). The ideia is, you have an cli object which you add scenes, and it will take care of everything, even the app loop.

# Features

- [x] Regular scene
- [x] Table scene
- [ ] Auth scene

# Dependencies

* Pandas

Pandas is required to make and show the tables

# How it works

1. Import and create the cli object.
  ```python
  from Cli import cli
  
  cli = cli()
  ```
2. Create as many scenes as you want.
  ```python
  wellcome_scene = scene("wellcome_scene", ["See information", "Go to table"], "Wellcome to the app, fell free to explore", ["info_scene", "info_table"])
  info_scene = scene("info_scene", ["Back to the wellcome scene"], "This is an example app :)", ["wellcome_scene"])
  info_table = table_scene("info_table", ["Back to the wellcome scene"], {"Column1": ["Line1", "Line2", "Line3"]}, ["wellcome_scene"])
  ```
3. Add the scenes on the cli object.
  ```python
  cli.add_scene("wellcome_scene", wellcome_scene)
  cli.add_scene("info_scene", info_scene)
  cli.add_scene("info_table", info_table)
  ```
4. Set the first scene which will be shown.
  ```python
  cli.set_first_scene_name("wellcome_scene")
  ```
5. Start the app loop.
  ```python
  cli.render_forever()
  ```

# Conclusion

I do lot's of cli programms to myself and a library for it will surely help me, i wish that can be helpful for you too. Feel free to make comments and constructive critcism.
