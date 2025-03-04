# ci-cd_pipeline
Github actions used for the deployment of application in staging environment

1. We need to clone the git repository where we are going to run the github actions pipeline.

2. Then create a directory with .github and inside that create one more dircetory named workflows.

3. Because in the ./github/workflows directory only we will configure yaml file for pipeline actions that needs to be done in the github actions.

4. I have configured a yaml file with the name of mainpipeline.yaml, In a way to test and build and push the image to the docker hub repository and then deploy that in your instance.

5. Maintain the docker_username, docker_password, server_ssh_privatekey, server_username and server_ip in the reposirtoy secrets and variables.

6. For maintaing the above details you need to use the secrets and variables that will be present in the repository settings. select reposirtory settings and then under settings choose actions. In the actions choose secrets and variables and maintain all the details that you need to pass through your configuration file.

7. Configure the Docker file in the .git directory to build the image.

8. Configure the applictaion file and place it in the same directory where you are maintaining the Docker file. In my case it is app.py.

9. In the requirements.txt file maintain the app name. In this case it is flask.

10. Once you setup all the above the settings. push the files to git hub repository.

11. Once the files ae pushed the ci/cd actions needs to take place.

12. To see the actions go to the repository and you will find the actions on the top.

13. There you can observe the pipeline that you have configured according to your setup.

14. Once the pipeline runs successfully you need to see the image in the dockerhub repository.

15. In our server when you run the docker ps our image will be present and we can access the application using the server ip and port number.

16. For every push the ci/cd runs its pipeline without getting any effect to the application once the pipeline finishes all its tasks, We can see the changes to our applications that we have made.
