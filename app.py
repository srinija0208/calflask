from flask import Flask, request, render_template

obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "welcome to flask"

@obj.route('/cal',methods=['GET'])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    ## json is a form of writing the data ( similarly, YMAL,XML ...... )


    if operation == "add":
        result=int(number1)+int(number2)
    elif operation  == "sub":
        result=int(number1)-int(number2)
    elif operation == "mul":
        result=int(number1)*int(number2)
    else:
        result=int(number1)/int(number2)

    return "the operation is {} and the result is {}".format(operation,result)

print(__name__)


if __name__=="__main__":
    obj.run()
