
import toml
import dropbox

with open('config.toml', 'r') as fo:
    config = toml.load(fo)

print(config)




def send_to_dropbox(fname):

    DBOX_DESTINATION = '/Apps/Raspberry Pie Camera'

    with open(fname, 'rb') as fo:
        data = fo.read()

    try:
        res = dbx.files_upload(data, '{}/{}'.format(DBOX_DESTINATION, fname))
    except dropbox.exceptions.ApiError as e:
        raise e


if __name__ == '__main__':

    dbx = dropbox.Dropbox(config['dropbox']['ACCESS_TOKEN'])

    mode = dropbox.files.WriteMode.overwrite

    fname = 'img_2018-09-08T21_14_09.025117.jpg'

    send_to_dropbox(fname)