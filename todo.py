""" Basic todo list using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete'
)


### Templates
render = web.template.render('templates')


class Index:

    def GET(self):
        """ Show page """
        switch = model.get_switch()
        form = self.form()
        return render.index(switch)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()