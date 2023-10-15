from flask import Flask, request, render_template

obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "welcome to flask"
print(__name__)

if __name__=="__main__":
    obj.run()
