from app import db


class Hh_vacancy(db.Model):
    __tablename__ = 'hh_vacancy'
    id = db.Column(db.Integer, primary_key=True)
    salary_from = db.Column(db.String(10))
    salary_to = db.Column(db.String(10))
    currency = db.Column(db.String(10))
    gross = db.Column(db.String(10))
    name = db.Column(db.String(20))
    area_name = db.Column(db.String(10))
    responsibility = db.Column(db.Text)
    requirement = db.Column(db.Text)
    vacancy_id = db.Column(db.Integer)
    employer_name = db.Column(db.String(20))
    employer_id = db.Column(db.String(20))
#    vacancy = db.relationship('Vacancy', backref='details')

    def __init__(self, salary_from=None, salary_to=None, currency=None, gross=None, name=None, area_name=None, responsibility=None, requirement=None, vacancy_id=None, employer_id=None, employer_name=None):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.gross = gross
        self.name = name
        self.area_name = area_name
        self.responsibility = responsibility
        self.requirement = requirement
        self.employer_id = employer_id
        self.employer_name = employer_name
        self.vacancy_id = vacancy_id

    def __repr__(self):
        return '<User {} {}>'.format(self.employer_name, self.name)
