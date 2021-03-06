#!/bin/bash
cd project/

fig stop
archive_filename=devblog-backup.tar

docker run --volumes-from project_data_1 -v $(pwd):/backup/ ubuntu tar cvf /backup/${archive_filename} /var/lib/postgresql/data /mezzanine-project/static/media

fig -f fig-production.yml up -d

bakthat backup --prompt no $archive_filename

rm $archive_filename
