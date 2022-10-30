import gql from "graphql-tag";



export const ALL_TASKS = gql`
  query {
    allTasks {
      id
      title
      isCompleted
    }
  }
`;

export const TASK_BY_ID = gql`
  query ($id: ID!) {
    taskById(id: $id) {
      id
      title
      content
      isCompleted
    }
  }
`;


export const CURRENT_USER = gql`
  query ($username: String!) {
    currentUser(username: $username) {
      id
      username
      firstName
      lastName
      email
    }
  }
`;
