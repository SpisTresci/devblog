#!/bin/bash
cd project/

fig stop
archive_filename=devblog-backup.tar

bakthat restore $archive_filename
docker run --volumes-from project_data_1 -v $(pwd):/backup ubuntu tar -vxf /backup/${archive_filename}

fig -f fig-production.yml up -d

rm $archive_filename
