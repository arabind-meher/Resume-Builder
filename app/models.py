from .extensions import db


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    educations = db.relationship("Education", backref="profile", lazy=True, cascade="all, delete-orphan")
    experiences = db.relationship("Experience", backref="profile", lazy=True, cascade="all, delete-orphan")
    skills = db.relationship("Skill", backref="profile", lazy=True, cascade="all, delete-orphan")
    projects = db.relationship("Project", backref="profile", lazy=True, cascade="all, delete-orphan")
    applications = db.relationship("Application", backref="profile", lazy=True, cascade="all, delete-orphan")


class Education(db.Model):
    __tablename__ = "educations"

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    school = db.Column(db.String(150), nullable=False)
    degree = db.Column(db.String(150), nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)


class Experience(db.Model):
    __tablename__ = "experiences"

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)


class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(150), nullable=False)
    job_url = db.Column(db.String(500), nullable=True)
    date_applied = db.Column(db.Date, nullable=False)