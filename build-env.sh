
set -e
NAMESPACE=registry.gitlab.com/haboustak/gitlab-artifact-tools
REPOSITORY=build-env
TAG=1.0
FULL_NAME=$NAMESPACE/$REPOSITORY:$TAG

echo "Building image $REPOSITORY:$TAG..."
IMAGE_ID=`docker build -q -t $FULL_NAME - < Dockerfile.build-env`
echo "$FULL_NAME created"
