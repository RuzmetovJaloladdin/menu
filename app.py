from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

# Dummy data to simulate submitted menu items
menu_items = []

# Route to display the form for submitting menu items
@app.route('/submit', methods=['GET', 'POST'])
def submit_menu_item():
    if request.method == 'POST':
        # Get form data
        item_name = request.form['item_name']
        item_description = request.form['item_description']
        item_price = float(request.form['item_price'])

        # Add the menu item to the list
        menu_items.append({'item_name': item_name, 'item_description': item_description, 'item_price': item_price})

        # Redirect to the view page
        return redirect(url_for('view_menu_items'))

    # If it's a GET request, simply render the submit form
    return render_template('submit.html')

# Route to display the submitted menu items
@app.route('/view')
def view_menu_items():
    return render_template('view.html', menu_items=menu_items)

# Route to delete a menu item
@app.route('/delete/<int:item_index>', methods=['POST'])
def delete_menu_item(item_index):
    if request.method == 'POST':
        # Delete the menu item from the list
        del menu_items[item_index - 1]  # Subtract 1 because list indices start from 0

    # Redirect back to the view page
    return redirect(url_for('view_menu_items'))

# Route for the homepage
@app.route('/')
def index():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
