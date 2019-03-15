#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(argument_spec={})
    response= {"Hello": "World"}
    response['changed']= False
    response['failed']= False

    #module.exit_json(changed=False,failed=True, meta=response)

    module.exit_json(**response)

if __name__ == '__main__':
    main()
