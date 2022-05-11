from app import app
from flask import render_template, redirect, flash, url_for
from app.classes.data import Team
from app.classes.forms import TeamForm
from flask_login import current_user



@app.route('/team/new', methods=['GET', 'POST'])
# This means the user must be logged in to see this page
# This is a function that is run when the user requests this route.
def teamNew():
    # This gets the form object from the form.py classes that can be displayed on the template.
    form = TeamForm()

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully.
    # validate_on_submit() is a method of the form object. 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new post form. 
        # Post() is a mongoengine method for creating a new post. 'newPost' is the variable 
        # that stores the object that is the result of the Post() method.  
        newTeam = Team(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            name = form.name.data,
            division = form.division.data,
            league = form.league.data,
            war = form.war.data,
            wins = 0,
            losses = 0,
            playoffAppearances = 0,
            divisionWins = 0


            
        )
        # This is a method that saves the data to the mongoDB database.
        newTeam.save()

        # Once the new post is saved, this sends the user to that post using redirect.
        # and url_for. Redirect is used to redirect a user to different route so that 
        # routes code can be run. In this case the user just created a post so we want 
        # to send them to that post. url_for takes as its argument the function name
        # for that route (the part after the def key word). You also need to send any
        # other values that are needed by the route you are redirecting to.
        return redirect(url_for('team',teamID=newTeam.id))

    # if form.validate_on_submit() is false then the user either has not yet filled out
    # the form or the form had an error and the user is sent to a blank form. Form errors are 
    # stored in the form object and are displayed on the form. take a look at postform.html to 
    # see how that works.
    return render_template('teamform.html',form=form)


# This route enables a user to edit a post.  This functions very similar to creating a new 
# post except you don't give the user a blank form.  You have to present the user with a form
# that includes all the values of the original post. Read and understand the new post route 
# before this one. 
