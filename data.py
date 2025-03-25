from faker import Faker
from psuenv.models import College, Program, Organization, Student, OrgMembership

fake = Faker()


for _ in range(8):
    College.objects.create(name=fake.company())

for _ in range(10):
    college = College.objects.order_by('?').first()  
    Program.objects.create(name=fake.job(), college=college)


Organization.objects.create(name="ACS")
Organization.objects.create(name="SITE")


program = Program.objects.first()  
student1 = Student.objects.create(name="You", program=program)
student2 = Student.objects.create(name="Your Partner", program=program)


acs = Organization.objects.get(name="ACS")
site = Organization.objects.get(name="SITE")
OrgMembership.objects.create(student=student1, organization=acs)
OrgMembership.objects.create(student=student2, organization=site)
