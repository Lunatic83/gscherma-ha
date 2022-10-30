import gql from "graphql-tag";

export const USER_SIGNUP = gql`
  mutation ($username: String!, $password: String!, $email: String!) {
    createUser(username: $username, password: $password,  email: $email ) {
      user {
        id
        username
        email
      }
    }
  }
`;

export const USER_SIGNIN = gql`
  mutation ($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
      user {
        id
        username
        firstName
        lastName
        email
      }
    }
  }
`;

export const CREATE_TASK = gql`
  mutation ($title: String!, $content: String!,  $isCompleted: Boolean!) {
    createTask(title: $title, content: $content, isCompleted: $isCompleted) {
      task {
        id
      }
    }
  }
`;

export const UPDATE_TASK = gql`
  mutation ($taskId: ID!, $title: String!, $content: String!,  $isCompleted: Boolean!) {
    updateTask(taskId: $taskId, title: $title, content: $content, isCompleted: $isCompleted) {
      task {
        id
      }
    }
  }
`;

export const UPDATE_TASK_COMPLETE = gql`
  mutation ($taskID: ID!, $isCompleted: Boolean!) {
    updateTaskComplete(taskId: $taskID, isCompleted: $isCompleted ) {
      task {
        id
        isCompleted
      }
    }
  }
`;

