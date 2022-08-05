from flask import render_template
from datetime import date
from app import app

#Function that returns year.
def footer_year():
    today = date.today()
    year = today.strftime("%Y")
    return (year)


@app.errorhandler(400)
def bad_request__error(exception):
    page="400 Error Page"
    page_no="400"
    message1="Oops! Bad request received."
    message2="You entered wrong values"
    
    return render_template("view_sample.html", title="400 Error| Tissue Sample Collection", page=page, page_no=page_no, message1=message1, message2=message2, year=footer_year())
    # return jsonify(
    #     {
    #         "Message": "Sorry you entered wrong values kindly check and resend!"
    #     },
    #     {
    #         "status": 400
    #     }
    # )


@app.errorhandler(404)
def not_found_error(error):
    page="404 Error Page"
    page_no="404"
    message1="Oops! Page not found."
    message2="We could not find the page you were looking for."
    
    return render_template("error_page.html", title="404 Error| Tissue Sample Collection", page=page, page_no=page_no, message1=message1, message2=message2, year=footer_year())
    # return jsonify(
    #     {
    #         "Message": "Sorry the page your are looking for is not here kindly go back"
    #     },
    #     {
    #         "status": 404
    #     }
    # )


@app.errorhandler(405)
def method_not_allowed(error):
    page="405 Error Page"
    page_no="405"
    message1="Oops! Method not allowed."
    message2="You used wrong HTTP method."
    
    return render_template("error_page.html", title="405 Error| Tissue Sample Collection", page=page, page_no=page_no, message1=message1, message2=message2, year=footer_year())
    # return jsonify(
    #     {
    #         "Message": "Sorry the requested method is not allowed kindly check and resend !"
    #     },
    #     {
    #         "status": 405
    #     }
    # )


@app.errorhandler(500)
def internal_server_error(error):
    page="500 Error Page"
    page_no="500"
    message1="Oops! Something went wrong."
    message2="We will work on fixing that right away."
    
    return render_template("error_page.html", title="500 Error| Tissue Sample Collection", page=page, page_no=page_no, message1=message1, message2=message2, year=footer_year())
    # return jsonify(
    #     {
    #         "Message": "Bad request please check your input and resend !"
    #     },
    #     {
    #         "status": 500
    #     }
    # )
