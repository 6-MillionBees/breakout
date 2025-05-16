


class Test1:
  def __init__(self):
    self.running = True
    self.run()


  def run(self):
    while self.running:
      Test2().run(self.running)
      print("ran")


class Test2:
  def __init__(self):
    pass

  def run(self, running):



    runner = False


Test1()