from troposphere import Template, Ref, Output, GetAtt
from troposphere.iam import AccessKey, User

tpl = Template()
tpl.add_version('2010-09-09')
tpl.add_description(
    "Create a CircleCI user with access to S3 bucket."
)

# Resources
superuser = tpl.add_resource(User(
    title='czpycon2015circleci',
))

access_keys = tpl.add_resource(AccessKey(
    "Troposphere",
    Status="Active",
    UserName=Ref(superuser))
)

# Outputs
tpl.add_output(Output(
    "AccessKey",
    Value=Ref(access_keys),
    Description="AWSAccessKeyId",
))

tpl.add_output(Output(
    "SecretKey",
    Value=GetAtt(access_keys, "SecretAccessKey"),
    Description="AWSSecretKey",
))

if __name__ == '__main__':
    print(tpl.to_json())
