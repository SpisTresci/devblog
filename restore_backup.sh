#!/bin/bash
docker run --volumes-from project_data_1 -v $(pwd):/backup ubuntu tar -vxjf /backup/devblog-backup-latest.tar.bz2
