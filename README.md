Adopted from [mtlynch/ingredient-phrase-tagger](https://hub.docker.com/r/mtlynch/ingredient-phrase-tagger/)

[See build and deploy quick start if necessary](https://cloud.google.com/run/docs/quickstarts/build-and-deploy#python_1)

## Setup

Install [Cloud SDK](https://cloud.google.com/sdk/) if you haven't already

## Deploy to Docker

Clone this repository first and cd to it

Build it

- `docker build .`

Find the image ID

- `docker images`

And tag it

- `docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`

- Example: `docker tag a1b2c3d4e5f6 ianspryn/ingredient-parser`

## Deploy to Cloud Run

See also: https://cloud.google.com/container-registry/docs/pushing-and-pulling

Run `docker pull ianspryn/ingredient-parser`

Tag the local image with the registry name using the command:

- `docker tag [SOURCE_IMAGE] [HOSTNAME]/[PROJECT-ID]/[IMAGE]`

 - Example: `docker tag ianspryn/ingredient-parser gcr.io/project-1a2b3/ianspryn/ingredient-parser`

Push it to Cloud Run

- `gcloud builds submit --tag [HOSTNAME]/[PROJECT-ID]/[IMAGE]`

- Example: `gcloud builds submit --tag gcr.io/project-1a2b3/ingredient-parser`