#!/usr/bin/env python3

import json
import yaml
import sys

def main():

    #Get pipeline id (project/pipeline-name) from script argument
    pipeline_id = sys.argv[1]

    # Read input JSON file
    with open( "targets.json", "r") as read_file:
        ansible_targets = json.load(read_file)
    # print(ansible_targets)

    # Generate list of pipelines to run
    pipelines_to_run = []
    for target in ansible_targets:
        pipeline = {}
        pipeline['pipeline_id'] = pipeline_id
        pipeline['variables'] = {}
        pipeline['variables']['OS_USER'] = target['os_user']
        pipeline['variables']['IP'] = target['ip']
        pipeline['variables']['SSH_KEY'] = target['ssh_key']
        pipeline['variables']['PLAYBOOK'] = target['playbook']
        pipelines_to_run.append(pipeline)
    
    # Write pipeline list to file
    with open("pipelines.yaml", "w") as write_file:
        yaml.dump(pipelines_to_run, write_file)

if __name__ == "__main__":
    main()
