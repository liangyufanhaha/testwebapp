from flask import request,render_template,url_for,flash,redirect
from app.forms.usecaeform import UserCaseform
from app.init import db
from app.model.user import UseCase

def addusecase():
    form=UserCaseform()
    if request.method=="POST":
         if form.validate_on_submit():
             use_case=UseCase(casename=form.casename.data,precondition=form.precondition.data,
                             usecasestep=form.usecasestep.data,preresult=form.preresult.data,
                             usecasetype=form.usecasetype.data,usecasestatus=form.usecasestatus.data,
                             usecasepriority=form.usecasepriority.data)
             try:
               db.session.add(use_case)
               db.session.commit()
               flash('Use case created successfully!')
               return redirect(url_for('tousecasepage'))

             except Exception as e:
                db.session.rollback()
                flash('Create failed: {}'.format(str(e)))
                return redirect(url_for('tocreateusecasepage'))
         else:
             print(form.errors)
    return render_template('createusecase.html',form=form)




def tousecasepage():
    usecaselist=UseCase.query.all()
    data=[{"id":usecase.id,"casename":usecase.casename,"precondition":usecase.precondition,"usecasestep":usecase.usecasestep,"preresult":usecase.preresult} for usecase in usecaselist]
    return render_template('usecaselist.html', usecases=data)


def editusecase():
     pass

def deleteusercae():
    pass

def tocreateusecasepage():
    return render_template("createusecase.html")
