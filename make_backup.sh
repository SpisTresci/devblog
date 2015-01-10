#!/bin/bash
timestamp=`date +"%Y%m%d%H%M%S"`
archive_filename=devblog-backup-${timestamp}.tar.bz2
docker run -i -t --volumes-from project_data_1 -v $(pwd):/backup/ ubuntu tar jcvf /backup/${archive_filename} /var/lib/postgresql/data /mezzanine-project/static/media
echo $archive_filename
ln -sf $archive_filename devblog-backup-latest.tar.bz2
