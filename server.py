from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class PostAndPatch(Resource):
    def post(self):
        parser.add_argument('shot_id', required=True, location='json', type=int,
            help="Must have a shot id.")
        parser.add_argument('shot_stage_id', required=True, location='json', type=int,
            help="Must have the current stage id.")
        parser.add_argument('shot_status_id', required=True, location='json', type=int,
            help="Must have a status id.")
        parser.add_argument('staff_id', required=True, location='json', type=int,
            help="Must have a staff id.")
        parser.add_argument('review_time', required=True, location='json',
            help="Must have a review time, which should be right now.")
        parser.add_argument('shot_version_name', required=True, location='json',
            help="Must have a shot version name.")
        parser.add_argument('shot_version_review_path', required=True, location='json',
            help="Must have a shot version review path.")
        args = parser.parse_args()

        return {'method': 'This is a POST request'}

    def patch(self):
        parser.add_argument('shot_id', required=True, location='json', type=int,
            help="Must have a shot id.")
        parser.add_argument('shot_stage_id', required=True, location='json', type=int,
            help="Must have the current stage id.")
        parser.add_argument('shot_status_id', required=True, location='json', type=int,
            help="Must have a status id.")
        parser.add_argument('staff_id', required=True, location='json', type=int,
            help="Must have a staff id.")
        parser.add_argument('review_time', required=True, location='json',
            help="Must have a review time, which should be right now.")
        parser.add_argument('shot_version_name', required=True, location='json',
            help="Must have a shot version name.")
        parser.add_argument('shot_version_review_path', required=True, location='json',
            help="Must have a shot version review path.")
        parser.add_argument('shot_version_id', required=True, location='json',
            help="Must have a shot version id.")
        args = parser.parse_args()

        return {'method': 'This is a PATCH request'}

api.add_resource(PostAndPatch, '/')
api.add_resource(PostAndPatch, "/wh1")
if __name__ == '__main__':
    app.run(debug=True)
    # Thread(target=init_func).start()
    # init()
    app.run(port=int(os.environ.get('PORT', 5000)))
