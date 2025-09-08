let getFetch = () => global.fetch;

export async function post(apiName, body) {
  const url = getURL(apiName);
  const fetch = getFetch();

  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      // ToDo: add auth token
    },
    body: JSON.stringify(body),
  });
  const myJson = await response.json();

  return myJson;
}

function getURL(apiName) {
  // ToDo: create config with URL, that works both locally and on server
  const apiURL = ''; 

  return apiURL + apiName;
}

export function get() {
  // ToDo: get method
}