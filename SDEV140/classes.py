class Page:
    def __init__(self, order_info, submit_fn):
        self.order_info = order_info
        self.on_submit = submit_fn

        submit_fn("once")


def do_submit(msg):
    print(msg)


page = Page("order info", do_submit)

page.on_submit("twice")
