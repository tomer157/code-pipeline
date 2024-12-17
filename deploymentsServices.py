import time
from datetime import datetime, timedelta
import threading
from abc import ABC, abstractmethod

# Abstract class for Deployment Targets
class DeploymentTarget(ABC):
    @abstractmethod
    def deploy(self, product_name):
        pass

# Artifactory deployment target
class ArtifactoryTarget(DeploymentTarget):
    def deploy(self, product_name):
        print(f"[{datetime.now()}] Deploying product: {product_name} to Artifactory")

# Nexus deployment target
class NexusTarget(DeploymentTarget):
    def deploy(self, product_name):
        print(f"[{datetime.now()}] Deploying product: {product_name} to Nexus")

# S3 deployment target
class S3Target(DeploymentTarget):
    def deploy(self, product_name):
        print(f"[{datetime.now()}] Deploying product: {product_name} to S3")

# Factory class for creating deployment targets
class DeploymentFactory:
    @staticmethod
    def get_target(target_type):
        if target_type.lower() == "artifactory":
            return ArtifactoryTarget()
        elif target_type.lower() == "nexus":
            return NexusTarget()
        elif target_type.lower() == "s3":
            return S3Target()
        else:
            raise ValueError(f"Unknown deployment target: {target_type}")