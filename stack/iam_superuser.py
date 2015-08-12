from troposphere import Template, Ref, Output, GetAtt
from troposphere.iam import AccessKey, User

tpl = Template()
tpl.add_version('2010-09-09')
tpl.add_description(
    "Create a superadmin user with all required privileges for this project. "
)

# Resources
superuser = tpl.add_resource(User(
    title='czpycon2015',
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
    Description="AWSAccessKeyId of superuser",
))

tpl.add_output(Output(
    "SecretKey",
    Value=GetAtt(access_keys, "SecretAccessKey"),
    Description="AWSSecretKey of superuser",
))

if __name__ == '__main__':
    print(tpl.to_json())
