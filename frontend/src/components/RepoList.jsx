import { useEffect, useState } from "react";
import { fetchRepositories } from "../api";

const RepoList = () => {
    const [repos, setRepos] = useState([]);

    useEffect(() => {
        fetchRepositories().then(setRepos);
    }, []);

    return (
        <div>
            <h2>Repositories</h2>
            <ul>
                {Object.entries(repos).map(([repo, count]) => (
                    <li key={repo}>{repo} - {count} issues</li>
                ))}
            </ul>
        </div>
    );
};

export default RepoList;
