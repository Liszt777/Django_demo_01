from django.shortcuts import render

#配置一个html页面显示的步骤
#1.配置url
#2.配置对应的views逻辑
#3.拆分静态（css, js, images）放入到static, html放入到templates下面
    #1.可以放到对应的app下面
    #2.也可以放入到全局的template和static目录下面
#4.配置全局的static文件访问路径的配置STATICFILES_DIR
    # (使用相对路径，例如STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')])



# Create your views here.
from apps.message_form.models import Message

# 通过请求方式（get, post）的不同来区分是展示页面，还是将页面数据送入数据库中
def message_form(request):
    # queryset 1.进行for循环 2.进行切片
    # queryset本身并没有执行sql操作
    # all_messages = Message.objects.all()
    # sliced_query = Message.objects.all()[:1]
    # print(all_messages.query)
    # print(sliced_query.query)

    # 2.filter 同样返回的是queryset结果集
    # all_messages = Message.objects.filter(name='bobby')
    # print(all_messages.query)
    # for message in all_messages:
    #     print(message.name)

    # 3.get 返回的是一个对象，数据不存在或者有多条数据存在会抛出异常
    # queryset 在进行for循环的时候才会查询数据库，而set在调用的时候立马就会查询数据库
    # message = Message.objects.get(name="bobby")
    # print(message.name)

    # 进行数据插入操作
    # message = Message()
    # message.name = 'bobby'
    # message.email = 'bobby@imooc.cn'
    # message.address = '北京市昌平区'
    # message.message = '留言'
    #
    # message.save() # 1.如果记录存在则更新，如果不存在则插入

    # 从html页面获取数据并送入数据库中
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message_text = request.POST.get('message', '')

        message = Message()
        message.name = name
        message.email = email
        message.address = address
        message.message = message_text
        message.save()
        return render(request, 'message_form.html', {
            'message': message,
        })

    if request.method == 'GET':
        var_message = {}
        all_messages = Message.objects.all()
        if all_messages:
            message = all_messages[0]
            var_message = {
                'message': message,
            }
        return render(request, 'message_form.html', var_message)
