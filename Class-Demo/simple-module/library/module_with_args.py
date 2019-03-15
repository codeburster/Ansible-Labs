#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
def main():
  argument_spec = {
	'name': {'type': 'str', 'required': True},
	'scores': {'type': 'list', 'required': False}, #, 'default': []},
	'state': {'choices': ['present','absent']}, #, 'default': 'present'},
	'options': {'type': 'dict'}, #, 'default': {}},
	}

  module = AnsibleModule(argument_spec=argument_spec, required_together=[['name','scores']], required_one_of=[['state','options']], supports_check_mode=False )

  name = module.params["name"]
  scores = module.params["scores"]
  state = module.params["state"]
  options = module.params["options"]

  result = dict()
  if state == 'present':
    result['task1'] = 'Directory Removed'

  result['failed'] = False
  result['changed'] = True
  result['name'] = name
  result['scores'] = scores
  result['state'] = state
  result['options'] = options
  module.exit_json(**result)

if __name__ == '__main__':
	main()
