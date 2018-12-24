import * as FileSaver from 'file-saver';


export const hostname = window.location.hostname;
export const port = location.port;
export const fullDomain = port ? hostname + ':' + port : hostname;
export const API_ROOT = location.protocol + '//' + fullDomain + '/';

type Headers = {
    'Accept'?: string,
    'Content-Type'?: string
}

const DEFAULT_HEADERS: Headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
};

export function request<T>(url: string, method: string, body?: Object, headers?: Partial<Headers>): Promise<T>{

    let requestHeaders: Headers = DEFAULT_HEADERS;
    if (headers){
        requestHeaders = Object.assign(DEFAULT_HEADERS, headers);
    }
    let requestContext: RequestInit = {
        method: method,
        credentials: 'same-origin',
        headers: requestHeaders as HeadersInit
    };
    if (body){
        requestContext.body = JSON.stringify(body);
    }

    return fetch(url, requestContext).then(resp => {
        // Request was good and something was returned
        if(resp.status >= 200 && resp.status < 204){
            const contentType = resp.headers.get("content-type");
            if(contentType && contentType.indexOf("application/json") !== -1){
                return resp.json().then(jsonResponse => {
                    return jsonResponse;
                })
            }
            else {
                const contentDisposition: string | null = resp.headers.get("content-disposition");
                let filename = 'download';
                if(contentDisposition){
                    const searchTerm: string = 'filename=';
                    filename = contentDisposition.substr(contentDisposition.indexOf(searchTerm) + searchTerm.length);
                }
                resp.blob().then(blob => {
                    FileSaver.saveAs(blob, filename);
                    return
                });
            }
        }
        // Request was good but nothing was returned
        else if(resp.status === 204){
            return
        }
        else {
            throw Error("Unable to post to server (Response Code: " + resp.status + ')');
        }
    }).catch(err => {
        console.error(err.message);
    })
}

export function post<T>(endPoint: string, body: Object, method?: string, responseType?: string, contentType?: string): Promise<T>{
    const requestMethod: string = method ? method: 'POST';
    const responseAccept: string = responseType ? responseType: 'application/json';
    const requestContext: Headers = {};
    if(responseAccept){
        requestContext['Accept'] = responseAccept;
    }
    if(contentType){
        requestContext['Content-Type'] = contentType
    }
    return request<T>(API_ROOT + endPoint, requestMethod, body, requestContext);
}

export function get<T>(endPoint: string, responseType?: string): Promise<T> {
    const responseAccept: string = responseType ? responseType: 'application/json';
    return request<T>(API_ROOT + endPoint, 'GET', undefined, {'Accept': responseAccept})
}