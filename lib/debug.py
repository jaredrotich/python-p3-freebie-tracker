#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    # Initialize database
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()
    session.commit()

    # Create test data
    company = Company(name="Hackathon Inc", founding_year=2020)
    dev = Dev(name="Alice")
    session.add_all([company, dev])
    session.commit()

    # Test Company.give_freebie()
    company.give_freebie(dev, "T-shirt", 10, session)

    # Test Dev.received_one()
    print(dev.received_one("T-shirt"))  # Should return True

    # Test Freebie.print_details()
    freebie = session.query(Freebie).first()
    print(freebie.print_details())  

    # Test oldest_company
    oldest = Company.oldest_company(session)
    print(f"Oldest company: {oldest.name}")

    import ipdb; ipdb.set_trace()