import tkinter

# enter your weight kg

# enter your height cm

# Enter both weight and height!

# Enter a valid number!

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

# result messages
result = ""
weight = 0.0
height = 0.0

# Weight
weight_label = tkinter.Label(text="Enter your weight (kg)", font=('Arial', 14, "normal"))
weight_label.config(padx=10, pady=10)
weight_label.pack()

weight_entry = tkinter.Entry(width=20, font=('Arial', 14, "normal"))
weight_entry.focus()
weight_entry.pack()

# Height
height_label = tkinter.Label(text="Enter your height (cm)", font=('Arial', 14, "normal"))
height_label.config(padx=10, pady=10)
height_label.pack()

height_entry = tkinter.Entry(width=20, font=('Arial', 14, "normal"))
height_entry.pack()

# message
msg = tkinter.Message(font=('Arial', 14, "normal"), width=200)


# Button
def show_result():
    global result
    global msg
    bmi_result = bmi_calculate()
    if type(bmi_result) == tuple:
        msg.config(text="Your BMI is {}. You are {}".format(bmi_result[0], bmi_result[1]))
    else:
        msg.config(text="{}".format(bmi_result))
    msg.pack()


def bmi_calculate():
    global weight
    global height

    if weight_entry.get() == '' and height_entry.get() == '':
        return "Enter both weight and height!"
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
    except:
        return "Enter a valid number!"
    bmi = float("{:.2f}".format(weight / (height ** 2)))
    return bmi, bmi_classification(bmi)


def bmi_classification(bmi_result):
    if bmi_result < 18.5:
        return "Under Weight"
    elif 18.5 <= bmi_result <= 24.9:
        return "Normal"
    elif 25 <= bmi_result <= 29.9:
        return "Over Weight"
    elif 30 <= bmi_result <= 34.9:
        return "Obesity(Class 1)"
    elif 35 <= bmi_result <= 39.9:
        return "Obesity(Class 2)"
    else:
        return "Extreme Obesity"


calculate_button = tkinter.Button(text="Calculate", font=('Arial', 14, "normal"), command=show_result)
calculate_button.pack()

window.mainloop()
